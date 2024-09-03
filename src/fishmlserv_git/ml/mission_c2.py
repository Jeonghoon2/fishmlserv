import typer
import pickle
import os
from sklearn.neighbors import KNeighborsClassifier

app = typer.Typer()


def load_model(model_path: str):
    file_name = "model.pkl"

    full_path = os.path.join(model_path, file_name)
    with open(full_path, "rb") as file:
        model = pickle.load(file)
    return model


@app.command()
def predict_fish(length: float = typer.Option(..., "--length", "-l"),
                 weight: float = typer.Option(..., "--weight", "-w")):
    file_path = __file__
    model_path = os.path.dirname(file_path)
    model = load_model(model_path)
    
    result = model.predict([[length, weight]])
    
    if result == 0:
        fish_name = "Bream"
    else:
        fish_name = "Smelt"

    print(f'예측되는 물고기는 {fish_name} !!')

if __name__ == "__main__":
    app()
