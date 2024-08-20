<template>
    <nav class="border-b-2 border-gray-200 bg-white lg:bg-blue-50">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto py-2 lg:py-[10px] pl-5 lg:pl-20">
            <router-link :to="{ name: 'Home' }">
                <span class="self-center text-2xl lg:text-[40px] font-bold whitespace-nowrap lg:leading-[60px] text-blue-700 font-logo">Web Speech</span>
            </router-link>
        </div>
    </nav>
</template>
