
package com.epam.java.command;

import com.epam.java.util.Logging;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import static java.lang.Math.atan;
import static java.lang.Math.tan;

public class CPUIntensive implements Command {

    private static final Logging.Logger LOGGER = Logging.getLogger();
    private ExecutorService executorService;

    @Override
    public void start(String[] args) throws Exception {
        final int cores = Runtime.getRuntime().availableProcessors();
        executorService = Executors.newFixedThreadPool(cores);
        for (int i = 0; i < cores; i++) {
            executorService.submit(() -> {
                LOGGER.info(String.format("Starting work on thread %d", i));
                while (!Thread.currentThread().isInterrupted()) {
                    double result = tan(atan(tan(atan(Math.random()))));
                }
            });
        }
    }

    @Override
    public void stop() throws Exception {
        if (executorService != null) {
            executorService.shutdown();
            executorService.awaitTermination(10, TimeUnit.SECONDS);
        }
    }
}
