import json
import random

FACT_ITEMS = "fact_items"

TEXT = "text"
CAT = "cat"
SUBCAT = "subcat"
FACT_ID = "fact_id"
FACT_RANK = "fact_rank"

FILEPATH_J = r".\static\facts.json"


class Fotd:
    def __init__(self, inputpath=FILEPATH_J):
        with open(inputpath, "r", encoding="utf-8") as f:
            self.content = f.read()
        self.content = json.loads(self.content)

    def __len__(self):
        return self.get_number_of_facts()

    @property
    def facts(self):
        return self.content[FACT_ITEMS]

    def get_number_of_facts(self):
        return len(self.facts)

    def get_random_fact(self):
        """return random fact object of json
        :return: randomly selected line(s), (i.e. a list of fact dictionaries)
        """
        rnd_fact = random.choice(self.facts)
        if rnd_fact.get(FACT_ID) is not None:
            rnd_fact = self._get_all_facts_by_fact_id(rnd_fact.get(FACT_ID))
        else:
            rnd_fact = [rnd_fact]
        return rnd_fact

    def _get_all_facts_by_fact_id(self, fact_id):
        ret_facts = []
        for fact in self.facts:
            if fact.get(FACT_ID) == fact_id:
                ret_facts.append(fact)
        ret_facts = sorted(ret_facts, key=lambda f: f[FACT_RANK])
        return ret_facts

    def get_total_number_of_facts(self):
        # NOTE
        # self.flj.get_number_of_facts() -> gives all fact ITEMs
        # some facts are split into multiple items
        # -> count either fact_rank 1 or None
        facts = self.facts
        counter = 0
        for fct in facts:
            if fct.get("fact_rank") == 1 or fct.get("fact_rank") is None:
                counter += 1
        return counter

    def get_random_fact_list(self):
        # fact which has multiple entries is list of strings to be put
        # into multiple <p>
        motds = self.get_random_fact()
        motds = [el["text"] for el in motds]
        return motds
