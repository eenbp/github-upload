import ForecastBatch_pb2
read_metric = ForecastBatch_pb2.ForecastBatch()

with open('forecast_indy_0_0_2.dop.bin', 'rb') as f:
   
    read_metric.ParseFromString(f.read())
#    print(read_metric)
with open("forecast_indy_0_0_2.dop.txt", "w") as fd:
    fd.write(str(read_metric))
