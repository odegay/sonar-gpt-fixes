package com.epam.java.util;

public class Logging {

    private static final Logger instance = new Logger();
    private static final String prefix = " >> ";

    public static Logger getLogger() {
        return instance;
    }

    public static class Logger {

        public void info(String message) {
            System.out.println(String.format("%s%s", prefix, message));
        }

        public void error(Throwable e) {
            e.printStackTrace();
        }
    }

}
