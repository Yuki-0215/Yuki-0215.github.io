"""
MCP Weather Server

一个基于 OpenWeatherMap API 的天气 MCP 服务器
提供获取当前天气信息和天气预报的功能
"""

import os
from typing import Dict, Any, List
from datetime import datetime
import requests
from dotenv import load_dotenv

from mcp.server.fastmcp import FastMCP

# 加载环境变量
load_dotenv()

# 创建 MCP 服务器
mcp = FastMCP("Weather")

# OpenWeatherMap API 配置
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not OPENWEATHER_API_KEY:
    print("警告: 未找到 OPENWEATHER_API_KEY 环境变量")
    print("请在 .env 文件中设置你的 OpenWeatherMap API 密钥")

OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"


def format_temperature(temp_kelvin: float) -> str:
    """格式化温度显示（开尔文转摄氏度）"""
    celsius = temp_kelvin - 273.15
    fahrenheit = celsius * 9/5 + 32
    return f"{celsius:.1f}°C ({fahrenheit:.1f}°F)"


def format_weather_info(weather_data: Dict[str, Any]) -> str:
    """格式化天气信息为易读的字符串"""
    main = weather_data.get("main", {})
    weather = weather_data.get("weather", [{}])[0]
    wind = weather_data.get("wind", {})
    clouds = weather_data.get("clouds", {})

    location = weather_data.get("name", "未知位置")
    country = weather_data.get("sys", {}).get("country", "")
    if country:
        location += f", {country}"

    # 基本天气信息
    description = weather.get("description", "").title()
    temp = format_temperature(main.get("temp", 0))
    feels_like = format_temperature(main.get("feels_like", 0))

    # 详细信息
    humidity = main.get("humidity", 0)
    pressure = main.get("pressure", 0)
    wind_speed = wind.get("speed", 0)
    wind_deg = wind.get("deg", 0)
    cloudiness = clouds.get("all", 0)

    # 可见度（以米为单位，转换为公里）
    visibility = weather_data.get("visibility", 0) / 1000

    result = f"""🌍 **{location}**

🌤️ **当前天气**: {description}
🌡️ **温度**: {temp}
🤒 **体感温度**: {feels_like}
💧 **湿度**: {humidity}%
🌪️ **气压**: {pressure} hPa
💨 **风速**: {wind_speed} m/s
🧭 **风向**: {wind_deg}°
☁️ **云量**: {cloudiness}%
👁️ **能见度**: {visibility:.1f} km"""

    # 添加日出日落时间（如果有的话）
    sys_info = weather_data.get("sys", {})
    if "sunrise" in sys_info and "sunset" in sys_info:
        sunrise = datetime.fromtimestamp(sys_info["sunrise"]).strftime("%H:%M")
        sunset = datetime.fromtimestamp(sys_info["sunset"]).strftime("%H:%M")
        result += f"\n🌅 **日出**: {sunrise}"
        result += f"\n🌇 **日落**: {sunset}"

    return result


def format_forecast_info(forecast_data: Dict[str, Any]) -> str:
    """格式化天气预报信息"""
    city = forecast_data.get("city", {})
    location = city.get("name", "未知位置")
    country = city.get("country", "")
    if country:
        location += f", {country}"

    forecasts = forecast_data.get("list", [])

    result = f"📅 **{location} - 5天天气预报**\n\n"

    # 按日期分组预报数据
    daily_forecasts: Dict[str, List[Dict[str, Any]]] = {}
    for forecast in forecasts:
        dt = datetime.fromtimestamp(forecast["dt"])
        date_key = dt.strftime("%Y-%m-%d")

        if date_key not in daily_forecasts:
            daily_forecasts[date_key] = []
        daily_forecasts[date_key].append(forecast)

    # 显示每天的天气预报
    for date_key, day_forecasts in list(daily_forecasts.items())[:5]:  # 只显示5天
        date_obj = datetime.strptime(date_key, "%Y-%m-%d")
        date_str = date_obj.strftime("%m月%d日 (%A)")

        result += f"**{date_str}**\n"

        # 获取当天的温度范围
        temps = [f["main"]["temp"] for f in day_forecasts]
        min_temp = format_temperature(min(temps))
        max_temp = format_temperature(max(temps))

        # 获取主要天气描述（出现频率最高的）
        descriptions = [f["weather"][0]["description"] for f in day_forecasts]
        main_desc = max(set(descriptions), key=descriptions.count).title()

        # 获取平均湿度和风速
        avg_humidity = sum(f["main"]["humidity"] for f in day_forecasts) / len(day_forecasts)
        avg_wind_speed = sum(f["wind"]["speed"] for f in day_forecasts) / len(day_forecasts)

        result += f"  🌤️ {main_desc}\n"
        result += f"  🌡️ {min_temp} - {max_temp}\n"
        result += f"  💧 湿度: {avg_humidity:.0f}%\n"
        result += f"  💨 风速: {avg_wind_speed:.1f} m/s\n\n"

    return result


@mcp.tool()
def get_current_weather(city: str) -> str:
    """
    获取指定城市的当前天气信息

    Args:
        city: 城市名称（英文或中文）

    Returns:
        格式化的当前天气信息
    """
    if not OPENWEATHER_API_KEY:
        return "❌ 错误: 未配置 OpenWeatherMap API 密钥。请设置 OPENWEATHER_API_KEY 环境变量。"

    print(f"正在获取 {city} 的当前天气信息...")

    try:
        response = requests.get(
            f"{OPENWEATHER_BASE_URL}/weather",
            params={
                "q": city,
                "appid": OPENWEATHER_API_KEY,
                "lang": "zh_cn"
            },
            timeout=10
        )

        if response.status_code == 404:
            return f"❌ 错误: 找不到城市 '{city}'。请检查城市名称是否正确。"
        elif response.status_code == 401:
            return "❌ 错误: API 密钥无效。请检查 OPENWEATHER_API_KEY 配置。"
        elif response.status_code != 200:
            return f"❌ 错误: API 请求失败 (状态码: {response.status_code})"

        weather_data = response.json()
        return format_weather_info(weather_data)

    except requests.RequestException as e:
        return f"❌ 网络错误: {str(e)}"
    except Exception as e:
        return f"❌ 未知错误: {str(e)}"


@mcp.tool()
def get_weather_forecast(city: str, days: int = 5) -> str:
    """
    获取指定城市的天气预报

    Args:
        city: 城市名称（英文或中文）
        days: 预报天数（1-5天，默认5天）

    Returns:
        格式化的天气预报信息
    """
    if not OPENWEATHER_API_KEY:
        return "❌ 错误: 未配置 OpenWeatherMap API 密钥。请设置 OPENWEATHER_API_KEY 环境变量。"

    if days < 1 or days > 5:
        return "❌ 错误: 预报天数必须在 1-5 天之间。"

    print(f"正在获取 {city} 的 {days} 天天气预报...")

    try:
        response = requests.get(
            f"{OPENWEATHER_BASE_URL}/forecast",
            params={
                "q": city,
                "appid": OPENWEATHER_API_KEY,
                "lang": "zh_cn"
            },
            timeout=10
        )

        if response.status_code == 404:
            return f"❌ 错误: 找不到城市 '{city}'。请检查城市名称是否正确。"
        elif response.status_code == 401:
            return "❌ 错误: API 密钥无效。请检查 OPENWEATHER_API_KEY 配置。"
        elif response.status_code != 200:
            return f"❌ 错误: API 请求失败 (状态码: {response.status_code})"

        forecast_data = response.json()
        return format_forecast_info(forecast_data)

    except requests.RequestException as e:
        return f"❌ 网络错误: {str(e)}"
    except Exception as e:
        return f"❌ 未知错误: {str(e)}"


@mcp.resource("weather://current/{city}")
def get_current_weather_resource(city: str) -> str:
    """获取指定城市当前天气的资源"""
    return f"当前天气信息资源: {city}"


@mcp.resource("weather://forecast/{city}")
def get_forecast_resource(city: str) -> str:
    """获取指定城市天气预报的资源"""
    return f"天气预报资源: {city}"


@mcp.resource("weather://api-status")
def get_api_status() -> str:
    """获取 API 状态信息"""
    if OPENWEATHER_API_KEY:
        return "✅ OpenWeatherMap API 密钥已配置"
    else:
        return "❌ OpenWeatherMap API 密钥未配置"


def main():
    """运行 MCP 服务器"""
    print("🌤️ 启动天气 MCP 服务器...")
    print("📍 支持的功能:")
    print("  - 获取当前天气 (get_current_weather)")
    print("  - 获取天气预报 (get_weather_forecast)")
    print()

    if not OPENWEATHER_API_KEY:
        print("⚠️  警告: 未配置 OpenWeatherMap API 密钥")
        print("请创建 .env 文件并添加以下内容:")
        print("OPENWEATHER_API_KEY=your_api_key_here")
        print()
        print("获取 API 密钥: https://openweathermap.org/api")
        print()

    mcp.run()


if __name__ == "__main__":
    main()
    
