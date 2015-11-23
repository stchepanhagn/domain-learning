#!/usr/bin/python

import pdb
import planning
import sys


def main(args):
    verbose = '-v' in args
    try:
        i = 1 + int(verbose)
        examples_file = args[i]
        domain_name = args[i+1]
    except:
        print "usage: {cmd} [-v] examples_file"\
            " domain_name".format(cmd=args[0])
        return

    examples = []
    print "Parsing examples..."
    with open(examples_file) as f:
        line = f.readline().replace('\n', '')
        while line:
            triple = line.split('|')
            example = (triple[0], triple[1], triple[2])
            examples.append(example)
            line = f.readline().replace('\n', '')
    print "Done!"
    if not f.closed:
        print "Warning: file stream is still open."

    print "Creating domain..."
    domain = planning.Domain(domain_name)

    for e in examples:
        preconditions = e[0].split(',')
        operators = e[1].split(',')
        effects = e[2].split(',')

        domain.add_all_predicates(preconditions)
        domain.add_all_predicates(effects)
        domain.add_actions(operators, preconditions, effects)

    print "Done!"
    if verbose:
        print str(domain)
    else:
        print "Outputting to file..."
        output_file_name = "{domain_name}.pddl".format(domain_name=domain_name)
        with open(output_file_name, 'w') as f:
            f.write(str(domain))
        print "Done!"


if __name__ == '__main__':
    main(sys.argv)
