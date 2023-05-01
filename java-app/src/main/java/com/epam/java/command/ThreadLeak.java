package com.epam.java.command;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadLeak implements Command {

    private final ExecutorService executorService = Executors.newCachedThreadPool();
    private final Object monitor = new Object();

    @Override
    public void start(String[] args) throws Exception {
        while (!Thread.currentThread().isInterrupted()) {
            executorService.submit(() -> {
                synchronized (monitor) {
                    try {
                        monitor.wait();
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            });
            synchronized (monitor) {
                monitor.wait(10);
            }
        }
    }

    @Override
    public void stop() throws Exception {
        executorService.shutdown();
    }
}
