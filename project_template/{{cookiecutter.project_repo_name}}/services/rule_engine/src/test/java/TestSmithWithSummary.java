import agents.Smith;
import com.mindsmiths.ruleEngine.testing.AgentTest;
import com.mindsmiths.ruleEngine.testing.AgentTestResult;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class TestSmithWithSummary extends AgentTest {

    @Test
    public void testHeartbeat() {
        AgentTestResult<Smith> result = runFromSummary("smith/test_heartbeat.json");
        result.assertRuleFired("Heartbeat");
    }
}
