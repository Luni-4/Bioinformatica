Bioinformatica
================

# Indice

1. [Informazioni](#1-informazioni)
2. [Modalità di lavoro](#2-modalità-di-lavoro)
  1. [Divisione dei compiti](#21-divisione-dei-compiti)
  2. [Link Utili](#22-link-utili)
3. [Input](#3-input)
  1. [Drosophila melanogaster](#31-drosophila-melanogaster)
  2. [Homo sapiens](#32-homo-sapiens)
4. [Output](#4-output)
5. [Idee](#5-idee)
6. [Dubbi](#6-dubbi)


-----------------

# 1. Informazioni

- Linguaggio di programmazione: Python
- Versione Python: 3.5
- Librerie Python
    - scikit-learn
    - numpy
    - scipy
    - matplotlib
    - python3-tk (sudo apt-get install python3-tk) 

# 2. Modalità di lavoro

## 2.1. Divisione dei compiti

FEDERICO:

- Fare in modo che le funzioni di load salvino e leggano automaticamente i file npz con le matrici sparse
- Stampare l'area sotto i grafici e salvarli automaticamente evitando la stampa su schermo
- usare Timer su Adaboost

MICHELE:

- Formattare i dati delle metriche per latex

## 2.2. Link Utili

- Dati: http://homes.di.unimi.it/valentini/DATA/ProgettoBioinf1617

- Specifiche progetto Valentini: https://homes.di.unimi.it/valentini/SlideCorsi/Bioinformatica1617/Bioinf-Project1617.pdf

- Salvataggio dei classificatori come oggetti: http://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/

- Buona spiegazione di AUPRC e AUROC: http://www.chioka.in/differences-between-roc-auc-and-pr-auc/

- Spiegazione sbilanciamento delle classi (Data Imbalance) e possibili metodi per risolverlo: http://www.chioka.in/class-imbalance-problem/

- Spiegazione Precision-Recall Curve su Quora: https://www.quora.com/What-is-Precision-Recall-PR-curve?share=1

- Metodi di scoring: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter


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

# 5. Idee

- Cercare una buona implementazione di Pegaso, possibilmente ottimizzata il più possibile
- SVM normali
- SVM con class_weight=‘balanced’
- Approfondire parametro C nelle SVM
- AdaBoost
- Adaboost con diversi parametri o classificatori (quali?)
- Fare grafici che mostrano come variano diverse metriche in funzione di quanto sono popolate le classi.

# 6. Dubbi

FEDERICO:

- Com'è lento adaboost! 5-fold parallelizzato ci mette mezzo minuto per ogni classe ---> Possiamo cercare di ridurre il tempo distribuendo il carico di lavoro tra più unita? Per farlo dovremmo fare in modo che più classi vengano computate in parallelo.

MICHI:

- Problema con lo sbilanciamento delle classi, troppe etichette negative a fronte di quelle positive. Dobbiamo bilanciare le classi, altrimenti le metriche producono
risultati non buoni e vengono mostrati warning

- Abbiamo deciso di non usare la soglia t, descritta dal prof nel suo documento, per le metriche, vero? 
Perché sia svm che adaboost, per ciascuna feature, restituiscono o 0 o 1 e non il valore di probabilità relativo all'appartenenza ad una o ad un'altra classe.
