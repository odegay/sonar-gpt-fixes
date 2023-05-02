
package com.epam.java.command;

public interface Command {

    void start(String[] args) throws CustomCommandException;

    void stop() throws CustomCommandException;
}

class CustomCommandException extends Exception {
    public CustomCommandException(String message) {
        super(message);
    }
}
