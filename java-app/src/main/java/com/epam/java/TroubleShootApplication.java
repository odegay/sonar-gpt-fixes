package com.epam.java;

import com.epam.java.command.*;
import com.epam.java.util.Logging;

import java.util.HashMap;
import java.util.Map;

public class TroubleShootApplication {

    private static final Logging.Logger LOGGER = Logging.getLogger();
    private static final Map<String, Command> COMMANDS = new HashMap<>();

    static {
        COMMANDS.put("heap", new Heap());
        COMMANDS.put("stack-overflow", new StackOverflow());
        COMMANDS.put("open-sockets", new OpenSockets());
        COMMANDS.put("thread-leak", new ThreadLeak());
        COMMANDS.put("cpu-intensive", new CPUIntensive());
        COMMANDS.put("dead-lock", new DeadLock());
        COMMANDS.put("blocking-read", new BlockingRead());
    }

    public static void main(String[] args) throws Exception {
        final Command command = findCommand(args);
        if (command == null) {
            printUsage();
            System.exit(1);
        }

        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try {
                command.stop();
            } catch (Exception e) {
                LOGGER.error(e);
                System.exit(1);
            }
        }));

        command.start(args);
    }

    private static Command findCommand(String[] args) {
        if (args.length < 1) {
            return null;
        }
        final String cmdName = args[0].toLowerCase();
        return COMMANDS.get(cmdName);
    }

    private static void printUsage() {
        final String commands = String.join("|", COMMANDS.keySet());
        LOGGER.info(String.format("Usage: java -jar {jarname} (%s)", commands));
    }
}
