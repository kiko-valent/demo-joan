# Directiva: App de Gestión de Limpieza (Gerente y Equipo)

## Objetivo
Mejorar la aplicación de gestión de turnos ("mint-fresh-app") para permitir una asignación más visual (con calendario completo), un sistema de acceso simple para las empleadas vía PIN de 4 dígitos, seguimiento de tiempo por casa (fichar entrada), y captura de evidencia fotográfica para tareas e incidencias (artículos rotos).

## Entradas / Requisitos
1. **Vista Gerente - Horarios**:
   - Reemplazar/mejorar el selector de fecha y hora actual por un calendario completo (mes, día, hora).
   - "Asignar y notificar": Guardar el turno asignado para que aparezca exclusivamente en la cuenta de ese empleado.
2. **Vista Gerente - Equipo**:
   - Al crear empleada: Pedir Nombre, Apellidos, Teléfono y un PIN de 4 dígitos.
   - El PIN será la contraseña de acceso, y el Nombre será el usuario.
   - **NUEVO**: Capacidad de Editar (nombre, teléfono, pin) y Borrar perfiles de miembros del equipo.
3. **Vista Empleada - Acceso y Dashboard**:
   - Login usando Nombre y PIN.
   - Mostrar en el dashboard *solo* las casas asignadas a esa empleada.
4. **Vista Empleada - Ejecución de Tarea**:
   - Botón de "Fichar llegada" que inicie el tiempo a correr.
   - Reporte de artículo roto: Acceso a cámara/galería para subir fotos.
   - Lista de tareas: Opción para adjuntar fotos a solicitud del gerente.

## Salidas Esperadas
- Pantallas modificadas en `mint-fresh-app/src/features`.
- Integración con base de datos (`Supabase`) para manejar la autenticación simple (Nombre + PIN) y asociación de turnos.
- Subida de imágenes a `Supabase Storage`.

## Restricciones / Casos Borde
- **Plataforma Web (Vercel/Expo Web)**: La app se usa como PWA. `DateTimePicker` de `@react-native-community` crashea o no tiene interfaz en web. **Solución implementada:** Se ha configurado para renderizar un elemento nativo `<input type="datetime-local">` condicionado a `Platform.OS === 'web'`. Además, para web, `window.confirm` se usa en lugar de `Alert.alert` si falla o si hay que crear diálogos de borrado.
- **Entorno del Agente**: En este sistema falta instalación de Python en el PATH global (`python` arroja error de Microsoft Store), por lo que las directivas de ejecutar scripts locales en `scripts/` se deben saltar o usar las herramientas nativas del agente (`replace_file_content`) para aplicar parches al código directamente.
- **Autenticación Fuerte**: Dado que el login es "Nombre + PIN", no es criptográficamente robusto, es puramente funcional/práctico. Las reglas de RLS en Supabase deben permitir acceso seguro basado en este esquema si se expone la DB pública.
- **Manejo del Tiempo**: Si la pestaña de la app se cierra, el cronómetro debería poder calcularse basado en `hora actual - hora de fichaje start` almacenada en base de datos.

## Pasos de Implementación
1. Confirmar estado de base de datos Supabase (Tablas de Turnos, Empleados, Storage).
2. Implementar registro de PIN en `TeamPerformanceScreen`.
3. Implementar selector de calendario en `ScheduleManagementScreen`.
4. Crear pantalla de Login simplificado para Empleados.
5. Filtrar trabajos por Empleado logueado.
6. Implementar Fichaje (cronómetro basado en timestamp en Supabase).
7. Implementar subida de fotos (`expo-image-picker`).
