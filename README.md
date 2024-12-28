# Trabajo_Final_G4
Contenido del proyecto de sistema web de gestión de sesiones terapéuticas - CEPTI

## Proyecto: Plataforma digital para administrar los servicios del Centro Psicopedagógico Terapéutico Integral – CEPTI

## Descripción General

Se propone desarrollar e implementar una plataforma digital integrada que centralice los procesos clave de CEPTI, incluyendo la programación automatizada de sesiones con asignación de terapeutas según disponibilidad, la gestión unificada de historiales clínicos e informes de evolución. Además, estandarizará los reportes mediante plantillas predefinidas, facilitará la comunicación interna con herramientas integradas y permitirá el acceso multiplataforma para el equipo.

## Pasos para Instalar y Ejecutar el Proyecto

### Requisitos Previos
- Contar con python v3.12
- Editor de código fuente: VSC

### Instalación
1. Paso 1: Descargar la carpeta (.zip) 'cepti_project' en algun directorio
2. Paso 2: Descomprimir el contenido del archivo descargado

### Ejecución
- Ubicarse dentro de la carpeta cepti_project y abrir con VSC (./cepti_project/)
- Abrir en VSC (usar VSC seleccionando la carpeta del proyecto
- Abrir una terminal
- Iniciar el entorno virtual con el comando: .\venv\Scripts\activate
- Abrir un nuevo terminal
- En el segundo terminal, se debe activar el servidor local de 'roles_service'
    USAR EL SIGUIENTE CÓDIGO: uvicorn roles_service.main:app --host 0.0.0.0 --port 8001 --reload
- En el primer terminal, se debe activar el servidor local de 'user_service'
    USAR EL SIGUIENTE CÓDIGO: uvicorn user_service.main:app --host 0.0.0.0 --port 8000 --reload
- Acabamos de activar el servicio en web
    VISUALIZAR EL RESULTADO A TRAVÉS DEL ENLACE: 127.0.0.1:8000/user_interface/index.html
- Para desactivar los servidores remotos, USAR EL COMANDO CTRL + C en ambas terminales
  
## Integrantes del equipo y sus Roles

| Nombre                        | Rol en el Proyecto           |
|-------------------------------|------------------------------|
| Cardenas Pilco Patricia       | Scrum Master                 |
| Leandro Barrientos Delinger   | Front/Back-End Developer     |
