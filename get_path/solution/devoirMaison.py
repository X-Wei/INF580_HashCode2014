#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# christoph durr - 2015

# INF580 Programmation par contraintes et programmation mathématiques
# devoir maison
# Google Hashcode 2014
# https://sites.google.com/site/hashcode2014/tasks

from heapq import *
from random import *
from os.path import *
from sys import *

def readval(fi, ty): return ty(fi.readline())
def readtab(fi, ty): return tuple(map(ty, fi.readline().split()))

class Instance:

    def __init__(self, filename):
        fi = open(filename, 'r')
        self.nb_noeuds, nb_rues, self.temps_lim, self.nb_veh, self.start = readtab(fi, int)
        #~ self.nb_veh = 1
        self.temps_lim*=8;
        self.coor = [readtab(fi, float) for _ in range(self.nb_noeuds)]
        self.graph = [[] for u in range(self.nb_noeuds)]
        # pour chaque arc a:
        self.dist = {} # dist[a]   mètres de la rue
        self.temp = {} # temps=[a] sec nécessaire à la traversée
        for _ in range(nb_rues):
            A,B,D,C,L = readtab(fi, int)
            self.dist[A,B] = L
            self.temp[A,B] = C
            self.graph[A].append(B)
            if D == 2:
                self.dist[B,A] = L
                self.temp[B,A] = C
                self.graph[B].append(A)
        self.tour = [[self.start] for i in range(self.nb_veh)]

    def random(self):
        T = 0
        veh = [(T, i, self.start) for i in range(self.nb_veh)]
        heapify(veh)
        while veh:
            # prochain véhicule
            T, i, a = heappop(veh)
            # préparer liste des possibilités
            b = choice(self.graph[a])
            next = T + self.temp[a,b] 
            if next <= self.temps_lim:
                self.tour[i].append(b)
                heappush(veh, (next, i, b))

    def write_tours(self, filename):
        fi = open(filename, 'w')
        fi.write("%d\n" % len(self.tour))
        for tour in self.tour:
            fi.write("%d\n" % len(tour))
            for u in tour:
                fi.write("%d\n" % u)
        fi.close()

    def read_tours(self, filename):
        fi = open(filename, 'r')
        C = readval(fi, int)
        assert C <= self.nb_veh   
        self.tour = [[] for i in range(C)]
        for i in range(C):
            vi = readval(fi, int)
            self.tour[i] = [readval(fi,int) for _ in range(vi)]
        score = 0
        seen = set()
        for tour in self.tour:
            a = None
            T = 0
            for b in tour:
                if a == None:
                    assert b == self.start
                else:
                    T += self.temp[a,b]
                    rue = (min(a,b),max(a,b))
                    if rue not in seen:
                        seen.add( rue )
                        score += self.dist[a,b]
                a = b
            assert T <= self.temps_lim
        return score

    def write_gpx(self, filename, veh = None):
        "veh permet de spécifier un véhicule dont le tour seul doit être exporté."
        fi = open(filename, 'w')
        fi.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
        fi.write("<gpx>\n")
        if veh == None:
            select = self.tour
        else:
            select = [ self.tour[veh] ]
        for tour in select:
            fi.write("<trk><trkseg>\n")
            for a in tour:
                fi.write('<trkpt lat="%f" lon="%f"></trkpt>' % self.coor[a])
            fi.write("</trkseg></trk>\n")
        fi.write("</gpx>\n")
        fi.close()

if __name__=="__main__":

    if len(argv)==2:
        G = Instance(argv[1])
        G.random()
        G.write_tours("random_tour.txt")
        G.write_gpx("random_tour.gpx")
    elif len(argv)==3:
        G = Instance(argv[1])
        print( "Le score de votre solution est %d" % G.read_tours(argv[2]) )
        out = splitext(argv[2])[0] + ".gpx"
        G.write_gpx( out )
        print ("Un fichier '%s' a été produit que vous pouvez importer dans http://umap.openstreetmap.co/fr/" % out)
    else:
        print("""\
Usage: ./devoirMaison.py paris_54000.txt  # pour lire l'instance et produire une solution aléatoire
       ./devoirMaison.py paris_54000.txt votre_solution.txt # pour tester votre solution et produire un fichier GPX
       """)
