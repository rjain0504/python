{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "import requests\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "H = 500\n",
    "W = 600"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_function(entry):\n",
    "    print(\"This is the entry:\",entry)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def format_response(weather):\n",
    "    try:\n",
    "        name = weather['name']\n",
    "        desc = weather['weather'][0]['description']\n",
    "        temp = weather['main']['temp']\n",
    "        final_res = 'City: %s \\nConditions: %s \\nTemperature(°F):%s' %(name,desc,temp)\n",
    "    except:\n",
    "        final_res = 'There was an error'\n",
    "    return final_res\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_weather(city):\n",
    "    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'\n",
    "    url = 'https://api.openweathermap.org/data/2.5/weather'\n",
    "    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}\n",
    "    response = requests.get(url, params=params)\n",
    "    weather = response.json()\n",
    "    label['text'] = format_response(weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "root = tk.Tk()\n",
    "canvas = tk.Canvas(root,height=H,width=W)\n",
    "canvas.pack()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "bg_image = tk.PhotoImage(file='landscape.png')\n",
    "bg_label = tk.Label(root, image=bg_image)\n",
    "bg_label.place(relwidth=1, relheight=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "frame = tk.Frame(root, bg='#80c1ff', bd=5)\n",
    "frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')\n",
    "\n",
    "entry = tk.Entry(frame, font=40)\n",
    "entry.place(relwidth=0.65, relheight=1)\n",
    "\n",
    "button = tk.Button(frame, text=\"Get Weather\", font=40, command=lambda: get_weather(entry.get()))\n",
    "button.place(relx=0.7, relheight=1, relwidth=0.3)\n",
    "\n",
    "lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)\n",
    "lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')\n",
    "\n",
    "label = tk.Label(lower_frame)\n",
    "label.place(relwidth=1, relheight=1)\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
