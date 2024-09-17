import java.time.LocalTime;
import java.time.temporal.TemporalAmount;

public record SimulationData(LocalTime trainDepartTime, TemporalAmount trainTravelTime, LocalTime passengerArrivalTime, boolean canCatchTrain) {
    LocalTime trainArrivalTime() {
        return trainDepartTime.plus(trainTravelTime);
    }
}
