@echo off
chcp 65001 >nul
echo ================================================
echo   大社区成本治理驾驶舱 - 启动服务
echo ================================================
echo.

:: 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python，请先安装 Python 3.8+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: 检查 HTML 文件
if not exist "内帐下钻分析.html" (
    echo [错误] 当前目录缺少「内帐下钻分析.html」
    echo 请把 HTML 文件放到同一目录后再运行
    pause
    exit /b 1
)

:: 安装依赖
echo [1/2] 检查并安装依赖...
pip install flask -q

:: 启动服务
echo [2/2] 启动服务中...
echo.
python app.py
pause
