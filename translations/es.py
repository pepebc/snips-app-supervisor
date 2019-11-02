"""
This module contains the result sentences and intents for the English version
of the Supervisor app.
"""

# Result sentences
RESULT_BACK = "Hola, ya he regresado"
RESULT_CONFIRM_REBOOT = "¿Realmente quieres reiniciar el sistema?"
RESULT_CONFIRM_SHUTDOWN = "¿Realmente quieres apagar el sistema?"
RESULT_DISABLE_APP = "OK, voy a desactivar la aplicación {} y reiniciar Snips."
RESULT_ENABLE_APP = "OK, voy a activar la aplicación {} y reiniciar Snips."
RESULT_OK = "OK"
RESULT_REBOOT = "OK, voy a reiniciar. Ahora regreso."
RESULT_RESTART_SERVICE = "OK, ahora reinicio el servicio {}."
RESULT_RESTART_ALL_SERVICES = "OK, ahra reinicio todos los servicios de Snips."
RESULT_SHUTDOWN = "OK, apago todo. Por favor, enciende pronto."
RESULT_SORRY = "Lo siento, he encontrado un error. Consulta los logs para resolverlo."
RESULT_SORRY_PERMISSIONS = "Lo siento, no pude cambiar los permisos de ejecución de los archivos de acción."

# Intents
INTENT_CONFIRM_REBOOT = 'koan:ConfirmReboot'
INTENT_CONFIRM_SHUTDOWN = 'koan:ConfirmShutdown'
INTENT_DISABLE_APP = 'koan:DisableApp'
INTENT_ENABLE_APP = 'koan:EnableApp'
INTENT_REBOOT = 'koan:Reboot'
INTENT_RESTART_SERVICE = 'koan:RestartService'
INTENT_SHUTDOWN = 'koan:Shutdown'

# Slot types
SLOT_TYPE_APP = 'koan/snips-app'
