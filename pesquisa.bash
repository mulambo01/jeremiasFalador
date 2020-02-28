#!/bin/bash
pesquisa=$1

linha=$(cat dicionario.dat | grep -n "^$pesquisa|" | cut -d: -f1)
qtlinhas=$(cat dicionario.dat | sed -n $[linha]p | cut -d'|' -f2)
cat dicionario.dat | sed -n $[linha],$[linha+qtlinhas]p

