from Prodotto import Prodotto

class Lotto:
    def __init__(self, id, batch_code, min_weight, max_weight, target_weight, checkweigher_mode, checkweigher_type):
        self._id = id
        self._batch_code = batch_code
        self._min_weight = min_weight
        self._max_weight = max_weight
        self._target_weight = target_weight
        self._checkweigher_mode = checkweigher_mode
        self._checkweigher_type = checkweigher_type

        self._min_meno = 0
        self._min = 0
        self._max = 0
        self._max_piu = 0

    #funzione per calcolare i range di peso in base al tipo di checkweigher
    def calcolaRange(self):
        #se il checkweigher è di tipo 1 (range percentuale)
        if self._checkweigher_mode == 1 and self._checkweigher_type == 1:
            self._min_weight = self._target_weight - (self._target_weight * self._min_weight / 100)
            self._max_weight = self._target_weight + (self._target_weight * self._max_weight / 100)
        #se il checkweigher è di tipo 0 (range assoluto)
        elif self._checkweigher_mode == 1 and self._checkweigher_type == 0:
            self._min_weight = self._target_weight - self._min_weight
            self._max_weight = self._target_weight + self._max_weight
