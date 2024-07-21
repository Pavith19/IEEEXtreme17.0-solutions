/* *
* Author: Pavith Bambaravanage
* URL: https://github.com/Pavith19
* */

import java.util.*;

public class Rumor {
    private static Map<String, List<String>> graph = new HashMap<>();
    private static Set<String> definiteNonSources = new HashSet<>();
    private static Set<String> possibleSources = new HashSet<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            String[] parts = line.split(" ");
            String p1 = parts[0];
            String p2 = parts[2];

            graph.putIfAbsent(p1, new ArrayList<>());
            graph.putIfAbsent(p2, new ArrayList<>());

            if (parts[1].equals("->")) {
                graph.get(p1).add(p2);
                definiteNonSources.add(p2);
            } else { // "??"
                graph.get(p1).add(p2);
                graph.get(p2).add(p1);
            }
        }

        for (String person : graph.keySet()) {
            if (!definiteNonSources.contains(person)) {
                possibleSources.add(person);
            }
        }

        List<String> sortedSources = new ArrayList<>(possibleSources);
        Collections.sort(sortedSources);

        for (String source : sortedSources) {
            System.out.println(source);
        }
    }
}
