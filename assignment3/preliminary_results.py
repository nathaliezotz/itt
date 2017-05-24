import csv
import statistics
import collections


def distraction_vs_nodistraction(in_list):
    dist = []
    no_dist = []

    for elem in in_list:
        if elem['distraction'] == 'yes':
            dist.append(int(elem['reaction_time_in_microseconds']))
        elif elem['distraction'] == 'no':
            no_dist.append(int(elem['reaction_time_in_microseconds']))

    print("mean dist", statistics.mean(dist))
    print("mean no dist", statistics.mean(no_dist))
    print("median dist", statistics.median(dist))
    print("median no dist", statistics.median(no_dist))
    print("max dist", max(dist))
    print("max no dist", max(no_dist))
    print()


def attentive_vs_pre_attentive(in_list):
    attentive = []
    pre_attentive = []

    for elem in in_list:
        if elem['mental_complexity'] == 'A':
            attentive.append(int(elem['reaction_time_in_microseconds']))
        elif elem['mental_complexity'] == 'P':
            pre_attentive.append(int(elem['reaction_time_in_microseconds']))

    print("mean attentive", statistics.mean(attentive))
    print("mean pre-attentive", statistics.mean(pre_attentive))
    print("median attentive", statistics.median(attentive))
    print("median pre-attentive", statistics.median(pre_attentive))
    print("max attentive", max(attentive))
    print("max pre-attentive", max(pre_attentive))
    print()


def errors_distraction_vs_no_distraction(in_list):
    dist = []
    no_dist = []

    for elem in in_list:
        if elem['distraction'] == 'yes':
            dist.append(elem['correct_key_pressed'])
        elif elem['distraction'] == 'no':
            no_dist.append(elem['correct_key_pressed'])

    print("dist", collections.Counter(dist))
    print("no_dist", collections.Counter(no_dist))
    # print("median dist", statistics.median(dist))
    # print("median no dist", statistics.median(no_dist))
    print()


def readfile(filepath):
    in_list = []
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            in_list.append(row)
    return in_list


def print_for_file(in_list):
    distraction_vs_nodistraction(in_list)

    attentive_vs_pre_attentive(in_list)

    errors_distraction_vs_no_distraction(in_list)


def main():
    in_list = readfile('reaction_time_results.csv')
    print_for_file(in_list)

    print()
    print()
    print()
    in_list = readfile('reaction_time_result_1.csv')
    print_for_file(in_list)

    print()
    print()
    print()
    in_list = readfile('reaction_time_result_2.csv')
    print_for_file(in_list)

if __name__ == '__main__':
    main()
