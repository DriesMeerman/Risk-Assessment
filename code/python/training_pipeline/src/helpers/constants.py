
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC


BEST_MODELS = {
    'MIN_DATA': [
        (0.7392378452213259, 'k-Nearest Neighbour', KNeighborsClassifier(algorithm='brute', n_neighbors=10)),
        (0.7348518803090451, 'Guassian Naive Bayes', GaussianNB()),
        (0.7348529474537926, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.7377758569172322, 'Decision Tree', DecisionTreeClassifier(criterion='entropy', max_depth=798, splitter='random')),
        (0.7348529474537926, 'Support Vector Machine (classifier)', SVC(kernel='linear', probability=True)),
        (0.7348529474537926, 'Stochastic Gradient Descent',SGDClassifier(alpha=1e-05, eta0=100.0, learning_rate='constant')),
        (0.7406944978016818, 'Multi-layer Perceptron', MLPClassifier(learning_rate='adaptive', max_iter=1000, solver='lbfgs'))
        ],
    'MIN_WITH_COMMITS': [
        (0.7275451402228198, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=12)),
        (0.35937593375165405, 'Guassian Naive Bayes', GaussianNB()),
        (0.7348529474537926, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.7260895547872113, 'Decision Tree', DecisionTreeClassifier(criterion='entropy', max_depth=798, splitter='random')),
        (0.7348529474537926, 'Support Vector Machine (classifier)', SVC(kernel='linear', probability=True)),
        (0.7341230204464934, 'Stochastic Gradient Descent', SGDClassifier(alpha=1e-05, eta0=100.0, learning_rate='invscaling', penalty='l1')),
        (0.7348540145985402, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, max_iter=1000, solver='lbfgs'))
        ],
    'MIN_WITH_LINKED': [
        (0.7991206727280489, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=9, weights='distance')),
        (0.7494504204550305, 'Guassian Naive Bayes', GaussianNB()),
        (0.7348529474537926, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.7574902889827977, 'Decision Tree', DecisionTreeClassifier(criterion='entropy', max_depth=798, splitter='random')),
        (0.7699118538438554, 'Support Vector Machine (classifier)', SVC(kernel='poly', probability=True)),
        (0.7830622785674648, 'Stochastic Gradient Descent', SGDClassifier(alpha=1e-05, eta0=100.0, learning_rate='adaptive', loss='log')),
        (0.8312684082468946, 'Multi-layer Perceptron', MLPClassifier(alpha=0.05, learning_rate='adaptive', max_iter=1000))
        ],
    'MIN_WITH_COMMITS_LINKED': [
        (0.8056985529517223, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=9, weights='distance')),
        (0.40247684295897895, 'Guassian Naive Bayes', GaussianNB()),
        (0.7348529474537926, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.7567635634097409, 'Decision Tree', DecisionTreeClassifier(criterion='entropy', max_depth=798, splitter='random')),
        (0.7772196610748282, 'Support Vector Machine (classifier)', SVC(kernel='poly', probability=True)),
        (0.77795278951637, 'Stochastic Gradient Descent', SGDClassifier(alpha=1e-05, eta0=100.0, learning_rate='adaptive', penalty='l1')),
        (0.8298074870875485, 'Multi-layer Perceptron', MLPClassifier(alpha=0.05, learning_rate='adaptive', max_iter=1000))
        ],
    'SHORT_DESC_MINIMAL': [
        (0.7903530114824775, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=17, weights='distance')),
        (0.4550678704059419, 'Guassian Naive Bayes', GaussianNB()),
        (0.7341198190122509, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9620213855807402, 'Support Vector Machine (classifier)', SVC(class_weight='balanced', kernel='poly', probability=True)),
        (0.9145430486191146, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, learning_rate='adaptive', loss='modified_huber', penalty='l1')),
        (0.9649368250309471, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, max_iter=1000, solver='lbfgs'))
        ],
    'SHORT_DESC_WITH_COMMITS': [
        (0.8064284799590216, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=17, weights='distance')),
        (0.4550678704059419, 'Guassian Naive Bayes', GaussianNB()),
        (0.7355828744610919, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.948867759422888, 'Support Vector Machine (classifier)', SVC(class_weight='balanced', kernel='poly', probability=True)),
        (0.9298757843513894, 'Stochastic Gradient Descent', SGDClassifier(alpha=1e-05, eta0=100.0, learning_rate='adaptive', loss='huber', penalty='l1')),
        (0.9612903914286934, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, learning_rate='adaptive', max_iter=1000, solver='lbfgs'))
        ],
    'SHORT_DESC_WITH_LINKED': [
        (0.8093524565672088, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=18, weights='distance')),
        (0.4550678704059419, 'Guassian Naive Bayes', GaussianNB()),
        (0.7421564861057754, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9503329491612242, 'Support Vector Machine (classifier)', SVC(class_weight='balanced', kernel='poly', probability=True)),
        (0.9678661373628719, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, loss='modified_huber', penalty='l1')),
        (0.961289324283946, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, max_iter=1000, solver='lbfgs'))
        ],
    'SHORT_DESC_WITH_COMMITS_LINKED': [
        (0.8151972083493405, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=18, weights='distance')),
        (0.4550678704059419, 'Guassian Naive Bayes', GaussianNB()),
        (0.7392346437870834, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9459523199726811, 'Support Vector Machine (classifier)', SVC(class_weight='balanced', kernel='poly', probability=True)),
        (0.9057775216630384, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, loss='modified_huber', penalty='l1')),
        (0.9700537840952748, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, learning_rate='adaptive', max_iter=1000, solver='lbfgs'))
        ],
    'DESC_MINIMAL': [
        (0.9452202586758868, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=18, weights='distance')),
        (0.4017575873991548, 'Guassian Naive Bayes', GaussianNB()),
        (0.7669900115251633, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9466843812694754, 'Support Vector Machine (classifier)', SVC(kernel='sigmoid', probability=True)),
        (0.49013638109873225, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, learning_rate='adaptive', loss='perceptron', penalty='elasticnet')),
        (0.991966534340718, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, learning_rate='adaptive', max_iter=1000, solver='lbfgs'))
        ],
    'DESC_WITH_COMMITS': [
        (0.9496030221539249, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=18, weights='distance')),
        (0.4017575873991548, 'Guassian Naive Bayes', GaussianNB()),
        (0.7640639006274812, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9569086950954027, 'Support Vector Machine (classifier)', SVC(kernel='sigmoid', probability=True)),
        (0.967135143210825, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, loss='modified_huber', penalty='l1')),
        (0.9897767533188202, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, learning_rate='adaptive', max_iter=1000, solver='lbfgs'))
        ],
    'DESC_WITH_LINKED': [
        (0.8780157510564732, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=3)),
        (0.4017575873991548, 'Guassian Naive Bayes', GaussianNB()),
        (0.7662590173731165, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9517938703205703, 'Support Vector Machine (classifier)', SVC(class_weight='balanced', kernel='poly', probability=True)),
        (0.9539868527767106, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, loss='modified_huber', penalty='l1')),
        (0.9890436248772784, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, learning_rate='adaptive', max_iter=1000, solver='lbfgs'))
        ],
    'DESC_WITH_COMMITS_LINKED': [
        (0.8977451231485039, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=4, weights='distance')),
        (0.4017575873991548, 'Guassian Naive Bayes', GaussianNB()),
        (0.7699097195543603, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9532611943484014, 'Support Vector Machine (classifier)', SVC(probability=True)),
        (0.9313431083792205, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, loss='modified_huber', penalty='l1')),
        (0.9853897212617919, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, max_iter=1000, solver='lbfgs'))
        ],
    'FULL_AND_SHORT_DESC': [
        (0.8173891236607334, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=14, weights='distance')),
        (0.5332362231613096, 'Guassian Naive Bayes', GaussianNB()),
        (0.7633318393306868, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9824721475220899, 'Support Vector Machine (classifier)', SVC(kernel='sigmoid', probability=True)),
        (0.993427455500064, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, learning_rate='adaptive', penalty='l1')),
        (0.9832052759636317, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', alpha=0.05, max_iter=1000, solver='sgd'))
        ],
    'FULL_AND_SHORT_DESC_WITH_COMMITS': [
        (0.7910904085030094, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=10, weights='distance')),
        (0.5332362231613096, 'Guassian Naive Bayes', GaussianNB()),
        (0.7662515473598839, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.9795503052033978, 'Support Vector Machine (classifier)', SVC(kernel='sigmoid', probability=True)),
        (0.993427455500064, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, learning_rate='adaptive', penalty='l1')),
        (0.990507747470867, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', max_iter=1000, solver='lbfgs'))
        ],
    'FULL_AND_SHORT_DESC_WITH_LINKED': [
        (0.8619477525931618, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=10, weights='distance')),
        (0.5332362231613096, 'Guassian Naive Bayes', GaussianNB()),
        (0.7655226874973322, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.978821445340846, 'Support Vector Machine (classifier)', SVC(kernel='sigmoid', probability=True)),
        (0.9941573825073633,     'Stochastic Gradient Descent', SGDClassifier( alpha=0.05, eta0=100.0, loss='modified_huber', penalty='l1')),
        (0.9795535066376404, 'Multi-layer Perceptron', MLPClassifier(activation='tanh', max_iter=1000, solver='lbfgs'))
        ],
    'FULL_AND_SHORT_DESC_WITH_COMMITS_LINKED': [
        (0.8663305160711999, 'k-Nearest Neighbour', KNeighborsClassifier(n_neighbors=10, weights='distance')),
        (0.5332362231613096, 'Guassian Naive Bayes', GaussianNB()),
        (0.7655216203525845, 'Multinominal Naive Bayes', MultinomialNB()),
        (0.977358389892005, 'Support Vector Machine (classifier)', SVC(kernel='sigmoid', probability=True)),
        (0.993427455500064, 'Stochastic Gradient Descent', SGDClassifier(alpha=0.05, eta0=100.0, learning_rate='adaptive', penalty='l1')),
        (0.983935202970931, 'Multi-layer Perceptron', MLPClassifier(learning_rate='adaptive', max_iter=1000, solver='lbfgs'))
    ]
}
