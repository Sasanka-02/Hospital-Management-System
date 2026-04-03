@echo off
echo ============================================
echo  Hospital Management System - FastAPI
echo  Starting all microservices...
echo ============================================

echo.
echo [1/7] Starting Patient Service on port 8081...
start "Patient Service :8081" cmd /k "cd patient-service && python -m uvicorn main:app --port 8081 --reload --log-level info"

timeout /t 2 /nobreak >nul

echo [2/7] Starting Doctor Service on port 8082...
start "Doctor Service :8082" cmd /k "cd doctor-service && python -m uvicorn main:app --port 8082 --reload --log-level info"

timeout /t 2 /nobreak >nul

echo [3/7] Starting Appointment Service on port 8083...
start "Appointment Service :8083" cmd /k "cd appointment-service && python -m uvicorn main:app --port 8083 --reload --log-level info"

timeout /t 2 /nobreak >nul

echo [4/7] Starting Pharmacy Service on port 8084...
start "Pharmacy Service :8084" cmd /k "cd pharmacy-service && python -m uvicorn main:app --port 8084 --reload --log-level info"

timeout /t 2 /nobreak >nul

echo [5/7] Starting Billing Service on port 8085...
start "Billing Service :8085" cmd /k "cd billing-service && python -m uvicorn main:app --port 8085 --reload --log-level info"

timeout /t 2 /nobreak >nul

echo [6/7] Starting Notification Service on port 8086...
start "Notification Service :8086" cmd /k "cd notification-service && python -m uvicorn main:app --port 8086 --reload --log-level info"

timeout /t 3 /nobreak >nul

echo [7/7] Starting API Gateway on port 8080 (LAST)...
start "API Gateway :8080" cmd /k "cd gateway && python -m uvicorn main:app --port 8080 --reload --log-level info"

echo.
echo ============================================
echo  All services started!
echo.
echo  Direct Swagger UI:
echo    Patient      : http://localhost:8081/docs
echo    Doctor       : http://localhost:8082/docs
echo    Appointment  : http://localhost:8083/docs
echo    Pharmacy     : http://localhost:8084/docs
echo    Billing      : http://localhost:8085/docs
echo    Notification : http://localhost:8086/docs
echo.
echo  Via Gateway (port 8080):
echo    http://localhost:8080/api/patients
echo    http://localhost:8080/api/doctors
echo    http://localhost:8080/api/appointments
echo    http://localhost:8080/api/pharmacy
echo    http://localhost:8080/api/billing
echo    http://localhost:8080/api/notifications
echo ============================================
pause
