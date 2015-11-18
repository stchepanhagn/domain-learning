
class Domain():

    def __init__(self):
        self.predicates = []
        self.actions = []

    def __str__(self):
        string = ['(define', ' ', '(domain learned)', '\n',
                  '\t', '(:predicates', '\n\t\t']

        for p in self.predicates:
            string += [str(p), '\n\t\t']

        string += [')', '\n\n\t']

        for a in self.actions:
            string += [str(a), '\n\n\t']

        string += ')'

        return ''.join(string)

    def add_predicate(self, predicate_str):
        self.predicates.append(InstantiatedPredicate.parse(predicate_str)

    def add_operator(self, operator_str, preconditions, effects):
        tokenized_str = operator_str.split('(')
        operator = tokenized_str[0]

        action = next(x for x in self.actions if x.operator is operator, None)

        if action is None:
            args = tokenized_str[1].replace(')','').split(',')
            n_args = len(args)

            action = Action(operator, n_args)

            for p in preconditions:
                
                
            
            self.actions.append(action)
        else:
        


class Predicate():
    def __init__(self, predicate, arity):
        self.predicate = predicate
        self.arity = arity
        self.terms = []
        for i in range(0, self.arity):
            # Add this to a predicate
            self.terms.append(['?x' + str(i), None])

    def add_term(self, term):
        self.terms.append(term)

    def __str__(self):
        string = ['(', self.predicate]
        for t in self.terms:
            string += ([' ', t[0]])
        string += ')'
        return ''.join(string)

    def print_grounded(self):
        string = ['(', self.predicate]
        for t in self.terms:
            string += ([' ', t[1]])
        string += ')'
        return ''.join(string)

    @classmethod
    def parse_grounded(cls, predicate_str):
        tokenized_str = predicate_str.split('(')
        predicate = tokenized_str[0]
        args = tokenized_str[1].replace(')','').split(',')
        arity = len(args)
        instantiated_predicate = Predicate(predicate, arity)
        for i in range(0, arity):
            # Add this to a predicate
            instantiated_predicate.terms[i][1] = args[i] 
        return instantiated_predicate

    @classmethod
    def parse(cls, predicate_str):
        tokenized_str = predicate_str.split('(')
        predicate = tokenized_str[0]
        args = tokenized_str[1].replace(')','').split(',')
        arity = len(args)
        instantiated_predicate = Predicate(predicate, arity)
        return instantiated_predicate

    
class Action():
    def __init__(self, operator, n_args):
        self.operator = operator
        self.n_args = n_args
        self.parameters = [] # TODO: Parse parameters
        self.preconditions = []
        self.positive_effects = []
        self.negative_effects = []

    def add_parameter(self, parameter):
        self.parameters.append(parameter)
        
    def add_precondition(self, fluent):
        self.preconditions.append(fluent)

    def add_positive_effect(self, effect):
        self.positive_effects.append(effect)

    def add_negative_effect(self, effect):
        effect_negated = ['(not', ' ', effect, ')']
        self.negative_effects.append(effect_negated)

    def __str__(self):
        string = ['(:action', ' ', self.operator, '\n', '\t', ':parameters', ' ', '(']

        for i in range(len(self.parameters)):
            string += self.parameters[i]
            if i < (len(self.parameters) - 1):
                string += ' '

        string += [')', '\n', '\t', ':precondition', ' ', '(', 'and', ' ']

        for p in self.preconditions:
            string += p
            string += ' '

        string += [')', '\n', '\t', ':effect', ' ', '(', 'and', ' ']

        for e in self.positive_effects:
            string += e
            string += ' '

        for e in self.negative_effects:
            string += e
            string += ' '

        string += [')', ')']

        return ''.join(string)