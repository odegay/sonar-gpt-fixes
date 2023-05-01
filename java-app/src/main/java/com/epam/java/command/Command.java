package com.epam.java.command;

public interface Command {

    void start(String[] args) throws Exception;

    void stop() throws Exception;
}
