class TransactionTypes:
    """
    Constantes para tipos de transação financeira.
    """
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

    CHOICES = [
        (INCOME, "Receita"),
        (EXPENSE, "Despesa"),
    ]


class Colors:
    """
    Paleta de cores padrão para categorias.
    Pode ser expandida no futuro.
    """
    PRIMARY = "#007BFF"
    SUCCESS = "#28A745"
    DANGER = "#DC3545"
    WARNING = "#FFC107"
    INFO = "#17A2B8"

    CHOICES = [
        (PRIMARY, "Azul"),
        (SUCCESS, "Verde"),
        (DANGER, "Vermelho"),
        (WARNING, "Amarelo"),
        (INFO, "Ciano"),
    ]
