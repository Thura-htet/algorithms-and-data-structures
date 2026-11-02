import random


class Clause:
    def __init__(self):
        self.clause = dict()


    def ajouter_litteral(self,lit,neg=False):
        # la mÃ©thode ajouter litteral doit ajouter le littÃ©ral lit
        # sous forme nÃ©gative si neg est Ã  True
        if not self.clause.get(lit):
            self.clause[lit] = (False, False)

        if neg:
            self.clause[lit][1] = True
        else:
            self.clause[lit][0] = True


    def forme_lit(tup):
        # détermine la forme du littéral en fonction de son tuple
        if tup[0]:
            return True
        if tup[1]:
            return False


    def evaluer(self,valeurs):
        # evaluer prend en paramÃªtre un dictionnaire de valeurs et
        # doit renvoyer True si la clause est vraie avec ces valeurs,
        # False si elle ne l'est pas et None s'il manque des valeurs 
        # pour pouvoir Ã©valuer la clause.
        for lit in valeurs:
            if forme_lit(self.clause[lit]) and valeurs[lit]:
                return True
        return False


    def litteraux(self):
        # cette mÃ©thode doit renvoyer une liste ou un itÃ©rateur sur
        # les littÃ©raux contenus dans la clause : si un littÃ©ral x, un
        # littÃ©ral Âx et un littÃ©ral y sont dans la clause, x et y devront 
        # Ãªtre Ã©numÃ©rÃ©s, mais une seule fois chacun.
        return self.clause.keys()

    def __str__(self):
        # cette mÃ©thode doit renvoyer la clause sous une forme lisible par
        # un Ãªtre humain
        debut = True
        res = ""
        for lit in self.clause.keys():
            if not debut:
                res += " ∨ "
            if self.clause[lit][1]:
        

    def est_tautologie(self):
        # Question Bonus
        pass

class Formule:
    def __init__(self):
        pass

    def ajouter_clause(self,clause):
        pass

    def litteraux(self):
        # cette mÃ©thode doit renvoyer une liste ou un itÃ©rateur sur
        # les littÃ©raux contenus dans la formule.
        pass

    def evaluer(self,valeurs):
        # evaluer prend en paramÃªtre un dictionnaire de valeurs et
        # doit renvoyer True si la clause est vraie avec ces valeurs
        # False si ce n'est pas possible et None si avec les valeurs
        # fournies on ne peut pas encore dÃ©cider.
        pass

    def __str__(self):
        # cette mÃ©thode doit renvoyer la formule sous une forme lisible par
        # un Ãªtre humain
        return ""

    def satisfiable(self):
        # Ã  l'aide de backtracking, cette mÃ©thode doit renvoyer false si la
        # formule n'est pas satisfiable et un dictionnaire associant littÃ©raux
        # et valeur rendant la formule vraie sinon.
        pass

    @staticmethod
    def random(nb_vars,nb_clauses,clause_maxsize,seed=None):
        # Une mÃ©thode statique pour gÃ©nÃ©rer des formules alÃ©atoires, la seed vous permettra 
        # de tester avec quelques exemples bien choisis
        if seed is not None:
            random.seed(seed)
        f = Formule()
        for i in range(nb_clauses):
            k = random.randint(1,clause_maxsize)
            c = Clause()
            for j in range(k):
                c.ajouter_litteral("x"+str(random.randint(0,nb_vars)),bool(random.getrandbits(1)))
            f.ajouter_clause(c)
        return f

    def simplifier(self):
        # Question Bonus
        pass


if __name__=="__main__":
    f = Formule.random(10,10,3)
    print(f)
    print(f.satisfiable())
    
    f = Formule.random(1,1,5,seed=10)
