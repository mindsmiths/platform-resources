import agents.Smith;
import com.mindsmiths.ruleEngine.testing.AgentTest;
import com.mindsmiths.ruleEngine.testing.AgentTestResult;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class TestSmith extends AgentTest {

    @Test
    public void testAgentId() {
        assertEquals("SMITH", new Smith().getId());
    }

    @Test
    public void testHeartbeat() {
        AgentTestResult<Smith> result = run(new Smith(), List.of());
        assertTrue(result.getRulesFired().contains("Heartbeat"));
    }
}
