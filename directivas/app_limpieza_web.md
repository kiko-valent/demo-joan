# Aplicación Web: Limpieza y Mantenimiento

## 1. Arquitectura y Stack Tecnológico
Esta aplicación es PURAMENTE WEB. No se utiliza React Native, Expo, ni frameworks móviles.
Se ha construido utilizando:
- **React 18+**
- **Vite** como empaquetador (rápido y ligero)
- **Vanilla CSS** para los estilos, sin Tailwind a menos que se requiera explícitamente.

## 2. Objetivo Principal
Proporcionar una interfaz web robusta y rápida para la gestión de limpiezas y mantenimientos, minimizando errores de conectividad o problemas asociados a emuladores/dispositivos móviles. Esta web app será subida a GitHub y posteriormente desplegada en Vercel.

## 3. Restricciones y Casos Borde
- **Restricción de Móvil:** **NO** usar módulos ni librerías exclusivas de React Native (e.g., `react-native`, `expo-file-system`, `expo-sharing`). Todo debe ser compatible con un entorno de navegador estándar.
- **Enrutamiento:** Utilizar `react-router-dom` para la navegación web, no React Navigation.
- **Estilos:** Priorizar Vanilla CSS. Evitar la importación de hojas de estilo globales masivas desde bibliotecas de terceros que puedan ensuciar el diseño limpio pedido.
- **Despliegue:** Asegurar que el comando `npm run build` genere una carpeta `dist` válida para Vercel.

## 4. Flujo de Trabajo (Protocolo Modificado para Desarrollo Web)
Dado que esta es una aplicación web en tiempo real:
- Las modificaciones de los componentes UI se hacen directamente en `mint-fresh-web/src/`.
- No hace falta crear scripts de Python en la carpeta global `scripts/` para modificar elfrontend, a menos que sean tareas puramente de scrapping/backend externo a la aplicación React.
- **Regla de Oro:** Siempre verificar los cambios con `npm run dev` en localhost antes de dar una tarea por finalizada.
