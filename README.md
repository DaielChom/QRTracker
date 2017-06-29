# QRTracker
### API - backend
En la presente sección se encuentra la API de QRtracker, la cual debe satisfacer los siguientes Diagramas.

###### 1. Modelo Entidad Relación

<div style="width:70%; margin: 0 auto;">
![MER](../../Documentacion/img/MER.png)
</div>


###### 2. Diagramas de Usuario.

<div style="width:70%; margin: 0 auto;">
![](../../Documentacion/img/diagrama_casos_de_uso_administrador.png)
</div>

<div style="width:70%; margin: 0 auto;">
![](../../Documentacion/img/diagrama_casos_de_uso_funcionario.png)
</div>

Teniendo en cuenta los diagramas anteriores la API debera cumplir con los sigientes endpoint.

Sección del Administrador:
- POST /paquetes
- POST /clientes

Seccion del funcionario:
- POST /funcionarios
- GET /funcionarios
- GET /monitorear
- PULL /monitorear
- GET /paquetes
