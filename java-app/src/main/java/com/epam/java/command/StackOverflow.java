package com.epam.java.command;

public class StackOverflow implements Command {

    @Override
    public void start(String[] args) throws Exception {
        recursiveCall();
    }

    @Override
    public void stop() throws Exception {

    }

    private void recursiveCall() {
        recursiveCall();
    }
}
