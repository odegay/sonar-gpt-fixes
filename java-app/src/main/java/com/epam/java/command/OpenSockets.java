package com.epam.java.command;

import com.epam.java.util.Logging;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.ArrayList;
import java.util.List;

public class OpenSockets implements Command {

    private static final Logging.Logger LOGGER = Logging.getLogger();
    private static final int PORT = 9083;

    private ServerSocket serverSocket;
    private Thread listenerThread;
    private List<Socket> acceptedSockets = new ArrayList<>();
    private List<Socket> submittedSockets = new ArrayList<>();

    @Override
    public void start(String[] args) throws Exception {
        serverSocket = new ServerSocket(PORT);
        listenerThread = new Thread(this::consume);
        listenerThread.start();

        try {
            LOGGER.info("Started socket flood");
            while (!Thread.currentThread().isInterrupted()) {
                final Socket socket = new Socket("localhost", PORT);
                submittedSockets.add(socket);
            }
        } catch (SocketException e) {
            LOGGER.info("Submitted " + submittedSockets.size() + " sockets before failure");
            LOGGER.error(e);
        }
    }

    @Override
    public void stop() throws Exception {
        Thread.currentThread().interrupt();
        listenerThread.interrupt();
        if (serverSocket != null) {
            serverSocket.close();
        }
    }

    private void consume() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                final Socket socket = serverSocket.accept();
                acceptedSockets.add(socket);
            }
        } catch (IOException e) {
            LOGGER.info("Accepted " + acceptedSockets.size() + " sockets before failure");
            LOGGER.error(e);
        }
    }
}
