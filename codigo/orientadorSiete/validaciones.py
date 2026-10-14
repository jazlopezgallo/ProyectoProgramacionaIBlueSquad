import re


def validar_legajo(legajo):
    """Retorna True si el legajo tiene exactamente cinco dígitos."""
    return re.fullmatch(r"[0-9]{5}", legajo) is not None


def validar_codigo(codigo):
    """Retorna True si el código tiene dos letras mayúsculas y cuatro dígitos."""
    return re.fullmatch(r"[A-Z]{2}[0-9]{4}", codigo) is not None


def validar_telefono(telefono):
    """Retorna True si el teléfono tiene formato NNNN-NNNN."""
    return re.fullmatch(r"[0-9]{4}-[0-9]{4}", telefono) is not None


def validar_correo(correo):
    """Retorna True si el correo tiene formato usuario@dominio.extension."""
    return re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", correo) is not None


def validar_importe(importe):
    """Retorna True si el importe es el símbolo $ seguido de uno o más dígitos."""
    return re.fullmatch(r"\$[0-9]+", importe) is not None


def validar_patente(patente):
    """Retorna True si la patente cumple el formato viejo (AAA123) o el nuevo (AA123AA)."""
    return re.fullmatch(r"[A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2}", patente) is not None