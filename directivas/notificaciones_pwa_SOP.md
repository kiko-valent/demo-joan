# Directiva: Notificaciones Push en PWA (Web)

## Objetivo
Implementar notificaciones web push en la aplicación React/Vite (PWA) para alertar a los usuarios de la gestión de limpiezas y eventos importantes.

## Consideraciones y Restricciones (iOS/Apple)
- **iOS Local:** Las notificaciones push web EN iOS **REQUIEREN** que la PWA sea instalada en la pantalla de inicio ("Añadir a la pantalla de inicio"). NO funcionan en el navegador Safari normal/nativo sin estar instalada como app.
- **Service Worker:** Se debe tener un Service Worker activo que escuche el evento `push`. Usando `vite-plugin-pwa`, se inyectará comportamiento en el SW.
- **Backend de Envío:** Se requiere un endpoint u orquestador para enviar los "push messages" (OneSignal, Firebase, o implementación VAPID propia). Por decidir.

## Pasos de Ejecución
1. Limpiar estructura de carpetas conflictivas antes de codificar.
2. Añadir botón/flow de solicitud de permisos `Notification.requestPermission()` en la interfaz frontend (ej. perfil o landing).
3. Suscribir al usuario obteniendo el token.
4. Al recibir el evento en background, el Service Worker ejecuta `self.registration.showNotification`.
5. Ejecutar commit de GitHub una vez listos y probados los cambios locales.
