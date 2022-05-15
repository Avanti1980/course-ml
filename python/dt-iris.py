import graphviz
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target


clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=4)
clf = clf.fit(X, y)
dot_data = tree.export_graphviz(
    clf, out_file=None,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    special_characters=True
)
graph = graphviz.Source(dot_data)
graph.render(view=True)
