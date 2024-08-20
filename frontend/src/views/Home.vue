<script setup>
import PrimaryButton from '../components/buttons/PrimaryButton.vue';
import HomeIllustration from '../components/HomeIllustration.vue';
import TopBar from '../components/TopBar.vue';
</script>
<template>
    <TopBar class="hidden lg:block lg:absolute lg:w-full lg:z-10" />
    <div class="max-w-screen-xl mx-auto flex flex-col lg:flex-row-reverse lg:justify-end h-screen">
        <div class="lg:mr-20 lg:max-w-full lg:w-fit lg:place-self-center lg:flex-grow">
            <h1 class="block lg:hidden text-xl font-bold py-8 text-center">Welcome to <span
                    class="text-blue-700 font-logo leading-[30px]">
                    Web Speech</span></h1>
            <HomeIllustration class="p-6 max-w-[450px] lg:max-w-[750px] mx-auto" />
        </div>
        <div
            class="place-self-center px-5 w-full rounded-t-[20px] bg-blue-50 lg:bg-white pt-10 lg:mt-0 lg:p-0 lg:ml-20 lg:w-fit h-full lg:h-fit">
            <h1 class="max-w-2xl mb-4 text-2xl font-bold">Web Speech API Demo</h1>
            <p class="max-w-2xl mb-6 font-normal text-slate-700 text-base lg:mb-8 lg:text-xl">
                The Web Speech API provides two distinct areas of functionality — speech recognition, and speech synthesis (also known as text to speech, or tts) — which open up interesting new possibilities for accessibility, and control mechanisms. This article provides a simple introduction to both areas, along with demos.</p>
            <div class="px-14 lg:px-0 mb-14 lg:max-w-60">
                <router-link :to="{ name: 'Read' }">
                    <PrimaryButton text="Get Started" class="w-full" />
                </router-link>
            </div>
        </div>
    </div>
</template>
