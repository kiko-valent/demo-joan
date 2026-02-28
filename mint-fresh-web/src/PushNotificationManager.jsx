import { useState, useEffect } from 'react';

export default function PushNotificationManager() {
  const [permission, setPermission] = useState('default');

  useEffect(() => {
    if ('Notification' in window) {
      setPermission(Notification.permission);
    }
  }, []);

  const requestPermission = async () => {
    if (!('Notification' in window)) {
      alert('Las notificaciones no están soportadas en este navegador.');
      return;
    }

    try {
      const result = await Notification.requestPermission();
      setPermission(result);
      if (result === 'granted') {
        console.log('Permisos de notificación concedidos.');
        // Aquí se puede agregar la lógica para suscribir al usuario a un backend o servicio
        // por ejemplo, obtener el PushSubscription usando el Service Worker.
      } else {
        console.log('Permisos de notificación denegados.');
      }
    } catch (error) {
      console.error('Error al solicitar permisos de notificación:', error);
    }
  };

  if (permission === 'granted') {
    return (
      <div className="notification-status granted">
        Notificaciones activadas ✓
      </div>
    );
  }

  if (permission === 'denied') {
    return (
      <div className="notification-status denied">
        Notificaciones bloqueadas
      </div>
    );
  }

  return (
    <div className="notification-prompt">
      <p>Habilita las notificaciones de limpieza y mantenimiento</p>
      <button onClick={requestPermission} className="btn-primary">
        Activar Notificaciones
      </button>
    </div>
  );
}
