class Prodotto:

    def __init__(self, id, plu, tipo, nome, descrizione, descrizione2, id_sezione, min_weight, max_weight, target_weight, percent_min_weight, percent_max_weight, batch_code, batch_code_enabled, checkweigher_mode, checkweigher_type):
        self._id = id
        self._plu = plu 
        self._tipo = tipo
        self._nome = nome
        self._descrizione = descrizione
        self._descrizione2 = descrizione2
        self._id_sezione = id_sezione
        self._min_weight = min_weight
        self._max_weight = max_weight
        self._target_weight = target_weight
        self._percent_min_weight = percent_min_weight
        self._percent_max_weight = percent_max_weight
        self._batch_code = batch_code
        self._batch_code_enabled = batch_code_enabled
        self._checkweigher_mode = checkweigher_mode
        self._checkweigher_type = checkweigher_type
