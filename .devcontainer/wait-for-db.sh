#!/bin/bash
# wait-for-db.sh - Aguarda o banco de dados ficar disponível

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z "$host" "$port"; do
  echo "Aguardando banco de dados em $host:$port..."
  sleep 1
done

echo "Banco de dados está disponível!"
exec $cmd