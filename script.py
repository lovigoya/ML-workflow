def get_data():
    print("donothing")

def build_model():
    print("do nothing")

def preprocess_data():
    print("do nothing")


def create_pipeline():
    get_data()
    preprocess_data()
    build_model()
    pipeline_obj = 5
    return pipeline_obj

def inference():
    pipeline = create_pipeline()
    # pipeline.predict()
    return 1

if __name__=="__main__":
    inference()

