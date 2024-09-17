import java.time.Duration;
import java.time.LocalTime;
import java.time.temporal.TemporalAmount;
import java.util.Random;

public class Sys {
    private LocalTime trainDepartTime;
    private TemporalAmount trainTravelTime;
    private LocalTime passengerArrivalTime;
    private Random random;

    public Sys(Random random) {
        this.random = random;
    }

    public SimulationData runSimulation() {
        this.trainDepartTime = getTrainDepartTime();
        this.trainTravelTime = getTrainTravelTime();
        this.passengerArrivalTime = getPassengerArrivalTime();

        var catchTrain = canPassengerCatchTrain();
        return new SimulationData(trainDepartTime, trainTravelTime, passengerArrivalTime, catchTrain);
    }

    private LocalTime getTrainDepartTime() {
        var randNum = random.nextInt(10); //[0-9]
        if (randNum < 7) return LocalTime.of(13, 0); // [0-6]
        if (randNum < 9) return LocalTime.of(13, 5); // [6-7]
        return LocalTime.of(13, 10); // [9]

    }

    private TemporalAmount getTrainTravelTime() {
        var originalTravelTime = Duration.ofMinutes(30);
        var offset = Duration.ofMinutes(random.nextInt(3)); // generate [0-2] minutes
        if (random.nextBoolean()) {
            return originalTravelTime.plus(offset);
        }
        return originalTravelTime.minus(offset);

    }
    private LocalTime getPassengerArrivalTime() {
        var randNum = random.nextInt(10); // generate [0-9]
        if (randNum < 3) return LocalTime.of(13, 28);
        if (randNum < 7) return LocalTime.of(13,30);
        if (randNum < 9) return LocalTime.of(13,32);
        return LocalTime.of(13, 34);
    }
    private boolean canPassengerCatchTrain() {
        var trainArrivalTime = trainDepartTime.plus(trainTravelTime);
        return passengerArrivalTime.compareTo(trainArrivalTime) <= 0; // passenger arrival time <= train arrival time
    }
}
