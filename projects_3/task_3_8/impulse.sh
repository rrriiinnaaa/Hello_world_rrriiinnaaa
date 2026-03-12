if [ $# -lt 2 ]
then
    echo "Ошибка: недостаточно аргументов!"
    echo "Использование: ./impulse.sh <имя_гена> <уровень_экспрессии>"
    exit 1
fi

# Присваиваем аргументы переменным
GENE_NAME=$1
EXPRESSION_LEVEL=$2

# Выводим результат
echo "Экспрессия гена $GENE_NAME составляет $EXPRESSION_LEVEL единиц"
