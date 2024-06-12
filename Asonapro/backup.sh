#!/bin/bash
# llamado al sistema para generar es respaldo de DB
# sudo chmod 777 backup.sh
# bash backup.sh
export FECHA=`date +%d_%m_%Y_%H_%M_%S`
export NAME=apolo_${FECHA}.sql
export DIR=/home/miguel/Escritorio/Respaldo
USER_DB=root
NAME_DB=Sistema_Gestion
cd $DIR
> ${NAME}

export PGPASSWORD=Me.182-f
chmod 777 ${NAME}
echo "procesando la copia de la base de datos"
pg_dump -U $USER_DB -h localhost --port 5432 -f ${NAME} $NAME_DB
echo "backup terminado"