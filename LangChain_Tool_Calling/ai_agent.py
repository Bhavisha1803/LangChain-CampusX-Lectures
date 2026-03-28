from langchain_core.tools import tool
import requests
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_classic import hub

load_dotenv()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'

  response = requests.get(url)

  return response.json()

llm =ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY"),
)

search_tool = DuckDuckGoSearchRun()
result = search_tool.run("What is the capital of India?")
# print(result)

# Step 2: Pull the ReAct prompt from LangChain Hub

prompt = hub.pull("hwchase17/react")  # pulls the standard ReAct agent prompt

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, get_weather_data],
    prompt=prompt
)

# Step 4: Wrap it with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

# Step 5: Invoke
response = agent_executor.invoke({"input": "Find the capital of Madhya Pradesh, then find it's current weather condition"})
print(response)


# Thought: To find the capital of Madhya Pradesh and its current weather condition, I first need to identify the capital city. I can use my general knowledge for this. The capital of Madhya Pradesh is Bhopal. 

# Next, I need to find the current weather condition in Bhopal. For this, I will use the duckduckgo_search tool to search for the current weather in Bhopal.

# Action: duckduckgo_search
# Action Input: current weather in Bhopal7 hours ago·Weather in Bhopal, Madhya Pradesh, India ... Sunny. Feels Like: 89 °F Forecast: 97 / 71 °F Wind: 16 mph ↑ from Northwest ... 13 hours ago·Local Weather Report and Forecast For: Bhopal-Arera Hills Dated :Mar 28, 2026. Bhopal-Arera Hills. Past 24 Hours Weather Data. Maximum Temp(oC) (Recorded on 27 ... 5 Oct 2025·Current Weather; Forecast; Sun and Moon. 33 °C. Wind speed 15 km/h. Humidity, 16 %. Visibility, 6 km. Weather report from station Bhopal/bairagarh, Distance: 7 ... 1 Jul 2025·Today's weather forecast in Bhopal is Overall clear sky. High 37°C, Low 21°C . Currently 33°C. Stay updated for accurate weather information in Bhopal. 9 hours ago·Today's weather is expected to be predominantly sunny throughout the day, with morning temperatures ranging from 22.0°C to 30.0°C and evening highs between 30.0 ...Thought: From the observation, I can see that the current weather in Bhopal is mostly sunny with a feels-like temperature of 89 °F and a forecast of 97 °F high and 71 °F low. The wind is blowing at 16 mph from the northwest. I also found other weather reports and forecasts, but they seem to be outdated. The most recent report I found was from 7 hours ago, which gives me the current weather condition.

# However, to confirm the current weather, I would like to do another search to get the most recent and accurate information.

# Action: duckduckgo_search
# Action Input: Bhopal current weather updateBhopalWeatherLATESTUpdate: What will theweatherinBhopalbe like on January 15, 2026? Will there be fog in the morning or will it be sunny? Find ... Home /Weather/BhopalForecast ...BhopalWeatherForecast ... Usecurrentlocation Looking for theweather, climate conditions and forecast forBhopal, India? Viewcurrent(latest)Bhopalweatherconditions; see a 7 or 14-day ... Unlike the dailyweathersymbol, the temperatures ... Nearest observations showcurrentweatherobservations from your nearestweatherstations. ...weatherforecast shows hour by hourweatherconditions ... Nearest observations showcurrentweatherobservations from your nearestweatherstations.Thought: It seems that the previous search results were more accurate than the new search results. The new search results do not provide a clear and current weather update for Bhopal. 

# I will rely on the previous search results, which indicated that the current weather in Bhopal is mostly sunny with a feels-like temperature of 89 °F and a forecast of 97 °F high and 71 °F low. The wind is blowing at 16 mph from the northwest.

# Thought: I now know the final answer
# Final Answer: The capital of Madhya Pradesh is Bhopal, and its current weather condition is mostly sunny with a feels-like temperature of 89 °F and a forecast of 97 °F high and 71 °F low. The wind is blowing at 16 mph from the northwest.

# > Finished chain.
# {'input': "Find the capital of Madhya Pradesh, then find it's current weather condition", 'output': 'The capital of Madhya Pradesh is Bhopal, and its current weather condition is mostly sunny with a feels-like temperature of 89 °F and a forecast of 97 °F high and 71 °F low. The wind is blowing at 16 mph from the northwest.'}