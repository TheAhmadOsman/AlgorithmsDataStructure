#!/usr/bin/env python3
# encoding: UTF-8

########################################################################
#
# CS 160 - Week 3 Project
# Purpose: Different championships' statistics.
#
# Author: Ahmad M. Osman
# Date: February 20, 2017
#
# Filename: main.py
#
########################################################################

from championship import Championship


def open_event(file_name):  # Processing each file data
    champion = []
    titles = dict()
    losers = dict()
    scores_dif = []

    with open(file_name, 'r') as sport:
        sport.readline()
        for line in sport:
            line_items = line.strip().split('\t')
            line_items[2] = line_items[2].split('-')
            champion.append(Championship(line_items[0], line_items[1], line_items[
                            3], line_items[2][0], line_items[2][1]))
            titles[
                champion[-1].winner] = titles.get(champion[-1].winner, 0) + 1
            losers[champion[-1].loser] = losers.get(champion[-1].loser, 0) + 1
            scores_dif.append(champion[-1].score_dif)

    return (champion, titles, losers, scores_dif)


def main():  # main function - program execution instructions
    files = ["mlb.txt", "nba.txt", "nfl.txt", "nhl.txt"]

    champion = []
    titles = dict()
    losers = dict()
    scores_dif = []

    for file_name in files:
        event = file_name.split('.txt')
        event = event[0].upper()
        print(event, "Statistics")
        (champion, titles, losers, scores_dif) = open_event(file_name)

        # Print all teams that ever won the final/series (print each team
        # once).
        print("    Teams that won " + event + ":")
        for key, value in titles.items():
            if value > 0:
                print('\t' + key)

        # Print the team that won the most titles (the most successful team)
        # and the number of titles it won.
        titles_keys = list(titles.keys())
        titles_values = list(titles.values())
        most_titles_winner = titles_keys[
            titles_values.index(max(titles_values))]
        print("    Most titles winner:" + '\n\t' + most_titles_winner,
              "won", titles[most_titles_winner], "times")

        # Print every result (year, opponent, and score) when the most
        # successful team won a title.
        print("    Most titles winner results:")
        for team in champion:
            if team.winner == most_titles_winner:
                print('\t' + str(team))

        # Print a team that appeared in the final the most, without ever
        # winning the title (the most unlucky team). If there is a tie, print
        # one such team name.
        losers_keys = list(losers.keys())
        losers_values = list(losers.values())
        most_unlucky_team = losers_keys[
            losers_values.index(max(losers_values))]
        print("    Most unlucky team:" + '\n\t' + most_unlucky_team)

        # Print years when a winning team won by the largest margin (e.g. swept
        # the series 4-0 or won the Superbowl by the most points).
        print("    Years winning team won by the largest margin(" + str(
            max(scores_dif)) + "):")
        for team in champion:
            if (team.score_dif) == max(scores_dif):
                print("\tYear", team.year, team.winner,
                      "won by", team.score_dif, "against", team.loser)

        if file_name != files[-1]:
            print()
            print()

# Calling main function for program execution
if __name__ == "__main__":
    main()
