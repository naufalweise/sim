import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        var random = new Random();
        var simDataList = new ArrayList<SimulationData>();
        for (int i = 0; i < 1000; i++) {
            var sys = new Sys(random);
            var simData = sys.runSimulation();
            simDataList.add(simData);
        }
        generateReport(simDataList);

    }

    private static void generateReport(List<SimulationData> simDataList) {
        var simDataStream = simDataList.stream();
        var canCatchTrainCount = simDataStream.filter(SimulationData::canCatchTrain).count();
        var probabilityCatchTrain =  canCatchTrainCount / (double) simDataList.size();
        System.out.printf("Simulation Count:%d%n", simDataList.size());
        System.out.printf("Can Catch Train Count: %d%n", canCatchTrainCount);
        System.out.printf("Probability Catch Train: %.2f%n", probabilityCatchTrain);
        System.out.println("First 10 simulation data:");
        for (int i = 0; i < 10; i++) {
            System.out.println(simDataList.get(i));
        }
    }
}
