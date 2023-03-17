import pandas as pd

class Capabilities:
    def get_cpk(self, data: pd.Series, limits: pd.Series) -> float:
        mean = pd.Series.mean(data)
        stdev = pd.Series.std(data)
        lsl = limits[0]
        usl = limits[1]

        return min(self.get_cpl(mean, stdev, lsl),self.get_cpl(mean, stdev, lsl))


    def get_cpl(self, mean: float, stdev: float, lsl: float):
        return (mean - lsl) / (3 * stdev)

    def get_cpu(self, mean: float, stdev: float, usl: float):
        return (usl - mean) / (3 * stdev)

data = pd.read_csv('test_data.csv')
limits = pd.read_csv('test_limits.csv')

index = 0
cpks = []

capabilities = Capabilities()
for column in range(len(data)+1):
    cpks.append(capabilities.get_cpk(data.iloc[index], limits.iloc[index]))
    index += 1

print(cpks)


    
