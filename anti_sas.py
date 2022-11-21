from inp.input import select_analysis, get_file_path
from jstat.model import Model
from jstat.da import DiscriminateAnalysis
from jstat.efa import ExploratoryFactorAnalysis
from jstat.slr import SimpleLinearRegression
from jstat.mlr import MultipleLinearRegression
from jstat.clust import ClusterAnalysis


models: dict[str, Model] = {
    "Discriminate Analysis": DiscriminateAnalysis(),
    "Exploratory Factor Analysis": ExploratoryFactorAnalysis(),
    "Simple Linear Regression": SimpleLinearRegression(),
    "Multiple Linear Regression": MultipleLinearRegression(),
    "Cluster Analysis": ClusterAnalysis(),
}


def main() -> None:
    a: str = select_analysis()
    m: Model = models[a]

    print(m)


if __name__ == "__main__":
    main()
