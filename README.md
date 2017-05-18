Bioinformatica
================

# Indice

1. [Informazioni](#1-informazioni)
2. [Modalità di lavoro](#2-modalità-di-lavoro)
  1. [Divisione dei compiti](#21-divisione-dei-compiti)
  2. [Caricamento su repository](#22-caricamento-su-repository)
3. [Input](#3-input)
  1. [Drosophila melanogaster](#31-drosophila-melanogaster)
  2. [Homo sapiens](#32-homo-sapiens)
4. [Output](#4-output)
5. [Idee](#5-idee)
6. [TODO](#6-todo)
  1. [Luni-4](#61-luni-4)
  2. [Fede](#62-fede)

-----------------

# 1. Informazioni

- Linguaggio di programmazione: Python
- Versione Python: 3.5
- Librerie Python
    - scikit-learn
    - numpy
    - scipy

- Librerie in forse: Shogun (altre che non mi vengono in mente)

# 2. Modalità di lavoro

## 2.1. Divisione dei compiti

Ogni componente, secondo me, deve occuparsi di un classificatore diverso. Le parti che vanno gestite insieme sono:

- L'acquisizione dei dati e la loro formattazione

- L'analisi dell'output dei due classificatori

- Fase di test e set-up sperimentale

Per quanto riguarda la la parte relativa alla combinazione degli output dei classificatori, ensemble, direi di farla solo se abbiamo tempo

## 2.2. Caricamento su repository

Entrambi i componenti del gruppo caricano i file e le relative revisioni del codice per mezzo di pull-request. 
Se la pull-request viene accettata da entrambi i componenti, verrà "mergiata" nel repository master.
All'interno di una pull-request si possono fare revisioni, nel caso in cui il codice non sia ritenuto valido.

Esempio: https://github.com/mbunkus/mkvtoolnix/pull/1838

# 3. Input

- OGNI ENTRY DELLA MATRICE É SEPARATA DA UN ALTRA PER MEZZO DI UN TAB
- TENIAMO A 0 I VALORI DELLE DIAGONALI DELLE MATRICI DI ADIACENZA (FINGIAMO CHE NON ESISTANO)


## 3.1. Drosophila melanogaster

- Matrice di adiacenza 3195 x 3195.Un entry della matrice contiene un valore che indica la similarità tra le proteine, individuate dagli indici della entry stessa.

- Matrice delle annotazioni. Un entry della matrice può assumere solo i valori 0 e 1. Il valore 0 significa che la proteina non è associata alla classe, al contrario con 1 la proteina è associata.
    - 3195 x 1951 per BP
    - 3195 x 234 per MF
    - 3195 x 235 per CC

## 3.2. Homo sapiens

- Matrice di adiacenza 19247 x 19247. Un entry della matrice contiene un valore che indica la similarità tra le proteine, individuate dagli indici della entry stessa.

- Matrice delle annotazioni. Un entry della matrice può assumere solo i valori 0 e 1. Il valore 0 significa che la proteina non è associata alla classe, al contrario con 1 la proteina è associata.
    - 19247 x 3958 per BP
    - 19247 x 899 per MF
    - 19247 x 601 per CC

# 4. Output

- Usare una 5-fold cross-validation per generare il training set e i test set, a partire dalle matrici di adiacenza e delle annotazioni in input.

- Provare diverse soglie t di accettazione secondo un determinato criterio (??).

- Calcolare la Precisione (Prec(t)) e la sensibilità (Rec(t)) per le soglie t stabilite precedentemente. Cercare delle librerie che consentono di calcolarle

- Calcolare la F-score gerarchica (convertire in python il file F-hier.R, scritto in R, altrimenti usare una funzione di una libreria per calcolarla)

- Cercare libreria python che calcola AUROC e AUPRC. 


# 5. Idee

- Al posto di caricare completamente la matrice delle adiacenze, essendo simmetrica, caricare solo la matrice triangolare corrispondente
- Verificare i tipi di dato che occupano meno spazio in python
- Non decomprimere il file zip fornito, ma leggere il file compresso e decomprimerlo in real time con Zlib oppure Gzip.
- Una volta che si è completata una sessione di apprendimento, è utile salvare su disco un file che contenga l'oggetto classificatore. Vedere http://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/


# 6. TODO

## 6.1. Luni-4


## 6.2. Fede 



 





