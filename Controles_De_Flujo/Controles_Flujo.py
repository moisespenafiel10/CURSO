{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOhLFtyuSbzMCuLwW64Y6XK"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PUV50W7h-2CI"
      },
      "outputs": [],
      "source": [
        "for numero in range (1,21):\n",
        "  print(numero)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##LISTAS\n",
        "### se separa con comas y entre corchetes [ ]"
      ],
      "metadata": {
        "id": "Mpe0E4PC_f3z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "vocales = ['a','e','i','o','u']\n",
        "\n",
        "for vocal in vocales:\n",
        "  print(vocal)\n"
      ],
      "metadata": {
        "id": "mdTu2MBN_ph8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "colores = ['amarillo','rojo','azul','marron','anaranjado',]\n",
        "clr = input('ingrese color : ')\n",
        "for color in colores:\n",
        "  if color == clr :\n",
        "    print(color)\n",
        "    print(f\"Se encontro el color:{color}\")\n",
        "    break\n",
        "  print(color)"
      ],
      "metadata": {
        "id": "_bxxGsnWCdKg"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
